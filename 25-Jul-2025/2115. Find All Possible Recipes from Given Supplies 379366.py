# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_exist = defaultdict(bool)
        recipe_map = defaultdict(int)
        for supply in supplies:
            supply_exist[supply] = True
        for idx, recipe in enumerate(recipes):
            recipe_map[recipe] = idx

        def dfs(recipe):
            if recipe in supply_exist:
                return supply_exist[recipe]
            if recipe not in recipe_map:
                return False

            supply_exist[recipe] = False
            for ngh in ingredients[recipe_map[recipe]]:
                if not dfs(ngh):
                    return False
            supply_exist[recipe] = True
            return True

        res = []
        for recipe in recipes:
            if dfs(recipe):
                res.append(recipe)
        return res
