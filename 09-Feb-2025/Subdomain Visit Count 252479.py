# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = {}
        result = []
        for domain in cpdomains:
            visits, domain = domain.split()
            subdomain = domain.split(".")
            for sub in range(len(subdomain)):
                s = ".".join(subdomain[sub:])
                if s in domain_map:
                    domain_map[s] += int(visits)
                else:
                    domain_map[s] = int(visits)

        for key in domain_map:
            res = f"{domain_map[key]} {key}"
            result.append(res)
        return result

        