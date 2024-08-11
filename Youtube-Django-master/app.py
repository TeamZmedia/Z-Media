import os
import sys
import datetime
from django.core.management import execute_from_command_line

def main():
    # Get the desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE'] if os.name == 'nt' else os.environ['HOME'], 'Desktop'))

    # Create a log file on the desktop with a timestamp
    log_file = os.path.join(desktop_path, f'youtube_django_log_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

    # Open the log file in write mode
    with open(log_file, 'w') as f:
        # Redirect stdout and stderr to the file
        sys.stdout = f
        sys.stderr = f

        # Set the Django settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')

        # Apply migrations
        try:
            print("Applying migrations...")
            execute_from_command_line(['manage.py', 'migrate'])
        except Exception as exc:
            f.write(f"Error applying migrations: {exc}\n")
            raise

        # Skip loading initial data since it's not available
        print("Skipping initial data loading...")

        # Run the Django development server
        try:
            print("Starting server...")
            execute_from_command_line(['manage.py', 'runserver'])
        except Exception as exc:
            f.write(f"Error starting server: {exc}\n")
            raise
        finally:
            # Output the server address to the log file and console
            f.write("Server is running. Go to http://127.0.0.1:8000 in your web browser.\n")
            print("Server is running. Go to http://127.0.0.1:8000 in your web browser.")

if __name__ == '__main__':
    main()
