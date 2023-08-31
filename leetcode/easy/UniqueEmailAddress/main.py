

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        count = 0
        finemail = []
        for emaillist in emails :
            print("email = {}".format(emaillist))
            local, domain = emaillist.split('@')[0], emaillist.split('@')[1]
            # local
            print("before local = {}, domain = {}".format(local, domain))
            if '.' in local :
                local = local.replace('.', '')
            if '+' in local :
                index = local.find('+')
                local = local[:index]
            
            # domain은 할 필요 x -> '.', '+'둘다 아무 적용이 없기 때문에

            print("after local = {}, domain = {}".format(local, domain))
            finemail.append(local+'@'+domain)

        result = list(set(finemail))
        print('result = {}'.format(result))
        return len(result)

sol = Solution()
# print(sol.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
# print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
