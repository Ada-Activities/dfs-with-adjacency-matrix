# DFS With Adjacency Matrix Activity

This repository is the classroom activity for the Graphs Pt. 1 Roundtable in Unit 4.

## Learning Goals 
- Practice converting a list of edges into an adjacency list.
  
## One-Time Activity Setup

Follow these directions once, at the beginning of the activity:


1. Navigate to the folder where you wish to save activities. This could be your `projects` folder, or you may want to create a new folder for all of your activities.

   If you followed Ada's recommended file system structure, you can navigate to your projects folder with the following command:

   ```bash
   $ cd ~/Developer/projects
   ```

   Or, if you want to create a new folder for all of your activities:

   ```bash
   $ cd ~/Developer
   $ mkdir activities
   $ cd activities
   ```

   If you've already created an activities directory, you can navigate to it with the following command:

   ```bash
   $ cd ~/Developer/activities
   ```

2. In Github click on the "Fork" button to fork the repository to your Github account.  This will make a copy of the activity in your Github account. 

3. "Clone" the activity into your working folder. This command makes a new folder named for the activity repository, and then puts the activity into this new folder.

   ```bash
   $ git clone <clone_url_for_the_activity>
   ```

   The `<>` syntax indicates a placeholder. You should replace `<clone_url_for_the_activity>` with the actual URL you'd use to clone this repository. If you click the green "Code" button on the GitHub page for this repository, you'll see a URL that you can copy to your clipboard.
 
   Use `ls` to confirm there's a new activity folder

4. Move your location into this activity folder

   ```bash
   $ cd <repository_directory>
   ```

   The `<repository_directory>` placeholder should be replaced with the name of the activity folder. If you're not sure what the folder is named, remember that you can use `ls` to list the contents of your current location.

5. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

6. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:
   
   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this activity with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

   Not all activities will have dependencies, but there will still be an included `requirements.txt` file.

Summary of one-time activity setup:
- [ ] Fork the activity repository
- [ ] `cd` into your working folder, such as your `projects` or `activities` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the folder for the activity
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Activity Development Workflow

1. When working on this activity, always ensure that your virtual environment is activated:

   ```bash
   $ source venv/bin/activate
   ```

2. If you want to work on another project from the same terminal window, you should deactivate the virtual environment when you are done working on the activity:

   ```bash
   $ deactivate
   ```

## Class Activity

### DFS With Adjacency Matrices
Problem Statement:

In the Learn lesson, you were shown how to write a recursive dfs algorithm to traverse a graph represented by an adjacency dictionary. For this activity, you have been provided with a recursive implementation of the dfs algorithm that will traversa agraph represented by an adjacency list. 

 You have been given two functions: `adj_matrix_dfs` and `dfs_helper`.

`adj_matrix_dfs` takes in two parameters:

- *g*: an adjacency matrix
- *s*: the index of node from which traversal starts

Your task is to modify the existing helper method to work with an adjacency matrix instead of an adjacency list! You should not have to modify `adj_matrix_dfs` for this activity. 

### Example 1
*Input*:

    adj_matrix = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    start_index = 1

*Output*: 

    [1, 0, 2, 3, 4]

Explanation:

- We start at index 1 which represents node 1 and gets added to our `visited` list.
- In the list at index 1, we find a connection at index 0 which gets added to our `visited` list.
- We move to the list at index 0 and loop through it. Even though there is a connection at index 1, we've already visited that node so it doesn't get added to the list. No other connections exist within this list so we jump back to index 1 and continue from where we left off. 
- In the list at index 1, we find a second connection at index 2 which gets added to our `visited` list. We now jump to the list at index 2. 
- We find two connections here. The connection to node 1 doesn't get added to our list, but the connection to node 3 does and we jump to the list at index 3. 
- Here we find two more connections at index 2 and 4. Node 2 has already been visited so we move past it. Node 4 has not been visited so we add it to our list and jump to the list at index 4. 
- All connections in list 4 have been visited so our recursion ends and we end up with a list that displays the order in which the nodes have been visited.

### Example 2
*Input*:

    adj_matrix = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0],
    ]

    start_index = 3

*Output*: 

    [3, 2, 1, 0, 4]
    
## Running Tests
Use the tests provided in the `test_convert_graph.py` file to verify that your code is working correctly. You can verify the tests are working in one of two ways:

1. Run `pytest` in the terminal (make sure you are in the venv!)
2. Set up the testing environment in the VSCode Testing Pane
   1. Click on the beaker icon and click `Configure Python Tests`
   2. Select `pytest` from the list that appears
   3. Select `tests` from the new list that appears.
3. Verify the tests show up in the Testing Pane.
4. Run the tests to make sure they are all passing!