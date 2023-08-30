class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # 10^4 <= box <= 10^9 : Bulky 
        # if mass == 100 : heavy
        # Bulky and Heavy -> category : Both
        # !Bulky and !Heavy -> category : Neither
        answer = ''
        category = []

        volume = length * width * height
        # size = 4 * (length + width + height)
        dem = max(length, width, height)


        if volume >= 10**9 or dem >= 10**4 : category.append('Bulky')
        if mass >= 100 : category.append('Heavy')

        if len(category) == 1 :
            answer = category[0]
        elif len(category) >= 2 :
            answer = 'Both'
        else :
            answer = 'Neither'


        return answer

sol = Solution()

print(sol.categorizeBox(1000, 35, 700, 300))
print(sol.categorizeBox(200, 50, 800, 50))
print(sol.categorizeBox(2909, 3968, 3272, 727))



