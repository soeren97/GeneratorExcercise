# [Generator excercise]
This exercise is designed to familiarize myself with generators and memory-efficient coding techniques. By implementing this exercise, I aim to gain a deeper understanding of how to write code that conserves memory resources and operates efficiently.

The code is executed from 'main.py' and includes a debugging mode that creates a new data file, even if one is found. Additionally, the code utilizes a profiler to analyze the performance of the two main functions. These functions are designed to process data one row at a time, with two currently implemented as a proof of concept.

The size of the dataset can also be set in 'main.py' with the variable 'num_rows'.

## Installation Guide

### Prerequisites:
- Anaconda installed
- pip installed (usually comes with Anaconda)

### Steps:

1. **Clone the Repository:**
git clone https://github.com/soeren97/GeneratorExcercise.git

2. **Navigate to the Repository Directory:**
cd */GeneratorExcercise

3. **Create a Virtual Environment (Optional but Recommended):**
conda create -n your-env-name python=3.9

4. **Activate the Virtual Environment:**
conda activate your-env-name

5. **Install Required Packages:**
pip install .

6. **Verify Installation:**
Ensure all dependencies are installed successfully without any errors.

7. **Deactivate Virtual Environment (If Created):**
conda deactivate

### Additional Notes:

- **Virtual Environment:** Creating a virtual environment is a good practice to isolate project dependencies from other projects and the system Python environment.
- **pip Install:** The `pip install .` command installs the necessary packages specified in the `setup.py` file from the current directory.