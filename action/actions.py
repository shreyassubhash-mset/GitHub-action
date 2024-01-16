import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip()

# Get the hash of the latest commit
latest_commit_hash = run_command("git rev-parse HEAD")

# Get the hash of the previous commit
previous_commit_hash = run_command("git rev-parse HEAD^")

# Get the details of the latest commit
latest_commit_details = run_command(f"git log -n 1 --pretty=format:'%h %s' {latest_commit_hash}")

# Get the details of the previous commit
previous_commit_details = run_command(f"git log -n 1 --pretty=format:'%h %s' {previous_commit_hash}")

# Display the results
print("Latest Commit:")
print(latest_commit_details)

print("\nPrevious Commit:")
print(previous_commit_details)

# Calculate the difference between the latest and previous commits
commit_diff = run_command(f"git diff {previous_commit_hash}..{latest_commit_hash}")

print("\nCommit Difference:")
print(commit_diff)