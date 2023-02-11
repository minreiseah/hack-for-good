

def calculate_similarity(list1, list2):
    if list1[0] == 'Part Time' and list2[0] == 'Full Time' :
        return 0
    else :
        set1 = set(list1)
        set2 = set(list2)
        return len(set1.intersection(set2)) / len(set1.union(set2))


def match_seekers_to_jobs(job_postings, job_seekers):
    results = {}
    for seeker_id, seeker_qualifications in job_seekers.items() :
        scores = []
        for job_id, job_requirements in job_postings.items():
            score = calculate_similarity(seeker_qualifications, job_requirements)
            scores.append((job_id, score))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        results[seeker_id] = scores
    return results

# Example data
job_postings = {
    'Job1': ['Full Time', 'Independent', 'University', 'Programming'],
    'Job2': ['Part Time', 'Independent', 'O level']
}

job_seekers = {
    'Seeker1': ['Full Time', 'Not Independent', 'University'],
    'Seeker2': ['Part Time', 'Independent', 'O level', 'Programming']
}

results = match_seekers_to_jobs(job_postings, job_seekers)
print(results)
