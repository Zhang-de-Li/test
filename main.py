"""Apriori算法的基本步骤为：
    1）扫描全部数据，产生候选项1项集的集合C1；
    2）根据最小支持度，由候选1项集的集合C1产生频繁1-项集，记为L1；
    3）利用L1连接来产生候选项集C2；
    4）对C2中的项进行判定挖掘出L2，即删除C2中那些支持度小于最小支持度的项，得到频繁2-项集；
    5）重复3）~ 4），直到无法发现更多的频繁k-项集为止。
    注意：每挖掘一层Lk就需要扫描整个数据库一遍。
"""


def loadDataSet():
    return [[1, 2, 5], [2, 4], [2, 3], [1, 2, 4], [1, 3], [2, 3], [1, 3], [1, 2, 3, 5], [1, 2, 3]]


def createC1(dataset):
    c1 = []
    max = 0
    for transaction in dataset:
        if max < len(transaction):
            max = len(transaction)
        for item in transaction:
            if [item] not in c1:
                c1.append([item])
    return list(map(frozenset, c1)), max


def frequent_k(dataset, Ck, min_support):
    fk = {}
    for i in dataset:
        for j in Ck:
            if j.issubset(i):
                if j in fk:
                    fk[j] += 1
                else:
                    fk[j] = 1
    # print(fk)
    retList = []
    supportData = {}
    # numItems = float(len(dataset))
    for s in fk:
        # support = fk[s] / numItems
        if fk[s] >= min_support:
            retList.append(s)
        # supportData[s] = support
    # print(supportData)
    # print(retList)
    return retList


def Link_k(retList, k):
    temp_dict = {}
    lenrl = len(retList)
    for i in range(lenrl):
        for j in range(i + 1, lenrl):
            Lk1 = retList[i] | retList[j]
            if len(Lk1) == k:
                temp_dict[Lk1] = 1
    return list(temp_dict)


if __name__ == '__main__':
    dataSet = loadDataSet()
    C1, max= createC1(dataSet)
    fki = frequent_k(dataSet, C1, 2)
    print(fki)
    Ck2 = Link_k(fki, 2)
    for i in range(2, max):
        ci = Link_k(fki, i)
        fki = frequent_k(dataSet, ci, 2)
        print(fki)
