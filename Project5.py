import time
from functools import reduce

# ----- Decorator to log time -----
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Processed in {time.time() - start:.4f} seconds")
        return result
    return wrapper
# ----- Generator for resumes -----
def resume_generator(resume_list):
    for resume in resume_list:
        yield resume.lower()

# ----- Pure function to get keywords -----
def extract_keywords(resume, keywords):
    return list(filter(lambda word: word in resume, keywords))

# ----- Main processor -----
@log_execution_time
def process_resumes(resumes, keywords):
    result = []

    for index, resume in enumerate(resume_generator(resumes)):
        matched_keywords = extract_keywords(resume, keywords)
        score = reduce(lambda acc, _: acc + 1, matched_keywords, 0)
        result.append({
            'Resume #': index + 1,
            'Matched Keywords': matched_keywords,
            'Score': score
        })

    # Sort by score
    result.sort(key=lambda x: x['Score'], reverse=True)
    return result

# ----- Sample resumes -----
resumes = [
    "Experienced Python developer with knowledge of Django, Flask, and REST APIs.",
    "Front-end engineer skilled in HTML, CSS, JavaScript, and React.",
    "Data analyst proficient in Python, Pandas, NumPy, and machine learning.",
    "Software engineer with C++, Java, and system-level programming experience."
]

# ----- Required keywords -----
keywords = ['python', 'pandas', 'numpy', 'django', 'machine learning', 'flask']

# ----- Run tool -----
filtered_resumes = process_resumes(resumes, keywords)

# ----- Display result -----
for res in filtered_resumes:
    print(f"Resume {res['Resume #']} | Score: {res['Score']} | Keywords: {res['Matched Keywords']}")