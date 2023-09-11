#!/bin/bash

# Step 1: Run the Python script (enc.py) using python3
python3 enc.py

# Step 2: Navigate to the directory containing your Git repository


# Step 3: Add all changes to the Git staging area
git add .

# Step 4: Commit the changes with a message
git commit -m "Automated commit"

# Step 5: Push the changes to the remote repository (change 'origin' and  'main' as needed)
git push origin main

