from loguru import logger
import scorecardpy as sc
import pandas as pd 

class Loggings:
    def __init__(self, log_file):
        logger.add(f"{log_file}", level="INFO", encoding="utf-8", enqueue=True)

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)


# connected subgraph
def linked_subgraph(dic):
    rst = []
    visited = []

    def dfs(key, dic, temp_rst):
        temp_rst.append(key)
        visited.append(key)
        for node in dic[key]:
            if node not in visited:
                dfs(node, dic, temp_rst)
        return temp_rst

    for key in dic.keys():
        if key not in visited:
            temp_rst = dfs(key, dic, [])
            rst.append(temp_rst)
    col_grp = [[i] *len(rst[i]) for i in range(len(rst))]     
    return rst, col_grp


if __name__ == "__main__":
    # load data
    data = sc.germancredit()

    # data2dic;  filter feature type in int
    type_df = pd.DataFrame(data.dtypes).reset_index()
    type_df.columns = ['var', 'type']
    int_col = type_df[type_df["type"] == "int64"]["var"].tolist()
    corr_met = data[int_col].corr()
    corr_deep = pd.melt(corr_met.reset_index(names="cols"), ["cols"])
    corr_deep.columns = ["col1", "col2", "cor"]
    corr_deep = corr_deep[corr_deep['cor'] > 0.2]
    dic = corr_deep.groupby("col1")["col2"].agg(list).to_dict()

    # return labels ; labels mapping
    rst, col_grp = linked_subgraph(dic)
    col_lt = [item for sub in rst for item in sub]
    col_grp = [item for sub in col_grp for item in sub]
    dic_grp = dict(zip(col_lt, col_grp))
    dic_grp