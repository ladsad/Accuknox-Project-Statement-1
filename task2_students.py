import requests
import matplotlib.pyplot as plt

def fetch_student_data():
    """
    Fetches student data (name and score) from a mock API.
    """
    # Using fakerapi.it to generate random student data
    url = "https://fakerapi.it/api/v1/custom?_quantity=10&name=name&score=number"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_and_visualize(students):
    """
    Calculates average score and creates a bar chart.
    """
    if not students:
        print("No student data to process.")
        return

    names = [s['name'] for s in students]
    scores = [s['score'] for s in students]
    
    # Calculate Average
    avg_score = sum(scores) / len(scores)
    print(f"Number of Students: {len(students)}")
    print(f"Average Score: {avg_score:.2f}")
    
    # Create Bar Chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, scores, color='skyblue')
    
    # Add a horizontal line for the average
    plt.axhline(y=avg_score, color='r', linestyle='--', label=f'Average: {avg_score:.2f}')
    
    plt.xlabel('Student Name')
    plt.ylabel('Test Score')
    plt.title('Student Test Scores')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    
    # Save chart
    output_file = 'student_scores_chart.png'
    plt.savefig(output_file)
    print(f"Chart saved as {output_file}")

if __name__ == "__main__":
    print("Fetching student data...")
    data = fetch_student_data()
    process_and_visualize(data)
