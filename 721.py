class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        rd=[]
        for account in accounts:
            cur=[account[0]]
            cset=set()
            for ele in account[1:]:
                if ele not in cset:
                    cset.add(ele)
                    cur.append(ele)
            rd.append(cur)
                
        
        hashmap={}
        for index,account in enumerate(rd):
            for email in account[1:]:
                if email not in hashmap:
                    hashmap[email]=[1,[index]]
                else:
                    hashmap[email][0]+=1
                    hashmap[email][1].append(index)
        
        candidates=set()
        for key in hashmap.keys():
            if hashmap[key][0]>1:
                for index in hashmap[key][1]:
                    candidates.add(index)
        
        merged={}
        res=[]
        for index,account in enumerate(rd):
            if index not in candidates:
                res.append(sorted(account))
            else:
                if account[0] not in merged:
                    merged[account[0]]=set(account[1:])
                else:
                    for email in account[1:]:
                        if email not in merged[account[0]]:
                            merged[account[0]].add(email)
        
        for key,value in merged.iteritems():
            res.append([key]+sorted([ele for ele in value]))
            
        
        return res
