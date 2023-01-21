class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict ={}
        for domain in cpdomains:
            domainList = domain.split(" ")
            subdomainList = domainList[1].split(".")
            for i in range(len(subdomainList)):
                subdomain = ".".join(subdomainList[i:])
                domainDict[subdomain] = int(domainList[0])+domainDict.get(subdomain,0)
        res = []
        for key,val in domainDict.items():
            res.append(str(val) + " " + key)
        return res
            