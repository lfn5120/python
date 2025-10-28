def rank_students(names: list[str], math: list[int], eng: list[int]) -> list[str]:
    """Evaluates a list of tuples and rank them based on average scores DESC and ties are ordered ASC; O(n) time, O(nlogn) space"""
    grades = list(zip(math, eng)) # links each student's scores together for both disciplines
    avg = [] # declares average

    for math, eng in grades: # calculates average per student
        avg.append((math + eng)/2)
        
    class_list = list(zip(names, avg)) # combines the average score to their respective name and ranks from high to low
    ranking = sorted(class_list, key = lambda x: (-x[1],x[0]))
    
    print("FINAL CLASS RANKING:")

    for i, (str, int) in enumerate(ranking, start = 1):
        print(f"{i} - {str}: {int}")



names = ["Leo", "Alex", "Matte", "Simon", "Gazo", "Stella", "Rico", "Vera", "Msky", "Mari"] # declares students
math = [100, 40, 20, 30, 34, 59, 90, 100, 79, 94] # declares math scores
eng = [10, 45, 34, 12, 97, 96, 84, 96, 85, 23] # declares engineering scores


rank_students(names, math, eng)
