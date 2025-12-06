
import datetime
from project import Project

DEFAULT_FILE = "projects.txt"

DATE_FORMAT = "%d/%m/%Y"

def parse_date(date_str: str) -> datetime.date:
    return datetime.datetime.strptime(date_str, DATE_FORMAT).date()

def load_projects(filename=DEFAULT_FILE):
    projects = []
    try:
        with open(filename, encoding='utf-8') as f:
            header = f.readline()  # skip header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                # Expected fields: name, start_date, priority, cost_estimate, completion_percent
                if len(parts) < 5:
                    continue
                name = parts[0].strip()
                start_date = parse_date(parts[1].strip())
                priority = int(parts[2].strip())
                cost = float(parts[3].strip())
                percent = int(parts[4].strip())
                projects.append(Project(name, start_date, priority, cost, percent))
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"No file named {filename} found. Starting with an empty project list.")
    return projects

def save_projects(projects, filename=DEFAULT_FILE):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("name\tstart_date\tpriority\tcost_estimate\tcompletion_percent\n")
        for p in projects:
            f.write(f"{p.name}\t{p.start_date.strftime(DATE_FORMAT)}\t{p.priority}\t{p.cost_estimate:.2f}\t{p.completion_percent}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]
    incomplete.sort()
    completed.sort()
    print("Incomplete projects:")
    if incomplete:
        for p in incomplete:
            print("  ", p)
    else:
        print("  None")
    print("Completed projects:")
    if completed:
        for p in completed:
            print("  ", p)
    else:
        print("  None")

def filter_projects_by_date(projects, date_after):
    filtered = [p for p in projects if p.start_date >= date_after]
    filtered.sort(key=lambda x: x.start_date)
    return filtered

def add_new_project(projects):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be blank.")
        return
    date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = parse_date(date_str)
    except ValueError:
        print("Invalid date format.")
        return
    try:
        priority = int(input("Priority: ").strip())
        cost = float(input("Cost estimate: ").strip())
        percent = int(input("Percent complete: ").strip())
    except ValueError:
        print("Invalid numeric input.")
        return
    projects.append(Project(name, start_date, priority, cost, percent))
    print("Project added.")

def update_project(projects):
    if not projects:
        print("No projects to update.")
        return
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        choice = int(input("Project choice: ").strip())
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(project)
    new_percent = input("New Percentage (leave blank to keep current): ").strip()
    new_priority = input("New Priority (leave blank to keep current): ").strip()
    if new_percent:
        try:
            project.completion_percent = int(new_percent)
        except ValueError:
            print("Invalid percentage - ignored.")
    if new_priority:
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority - ignored.")
    print("Project updated.")

def main():
    projects = load_projects()
    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")
    while True:
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            filename = input("Filename to load: ").strip()
            if filename:
                projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save: ").strip()
            if filename:
                save_projects(projects, filename)
            else:
                save_projects(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
            try:
                date_after = parse_date(date_str)
                filtered = filter_projects_by_date(projects, date_after)
                if filtered:
                    for p in filtered:
                        print(" ", p)
                else:
                    print("No projects match that date filter.")
            except ValueError:
                print("Invalid date format.")
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {DEFAULT_FILE}? (y/n): ").strip().lower()
            if save_choice in ('y', 'yes'):
                save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
