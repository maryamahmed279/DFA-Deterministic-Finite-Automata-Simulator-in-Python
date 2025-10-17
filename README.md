# DFA-Deterministic-Finite-Automata-Simulator-in-Python
A Python implementation of a Deterministic Finite Automaton (DFA) that allows users to construct automata, define transitions, and test input strings for acceptance or rejection interactively.
🧠 DFA (Deterministic Finite Automata) Simulator

A Python-based DFA (Deterministic Finite Automata) simulator that allows users to define states, inputs, and transitions, then test strings to determine if they are accepted or rejected — with step-by-step transition tracing.

🚀 Features

Interactive setup for states, inputs, and transitions

Input validation to prevent invalid configurations

Displays the DFA’s transition table clearly

Shows detailed transition trace for each input string

Tells whether the string is ACCEPTED ✅ or REJECTED ❌

📁 Project Structure
├── main.py         # Main program: handles user input and DFA setup  
├── functions.py    # Helper functions for validation and transitions  
└── README.md       # Project documentation  

⚙️ How to Run

Clone the repository:

git clone https://github.com/your-username/dfa-simulator.git
cd dfa-simulator


Run the program:

python main.py


Follow the prompts to:

Enter states

Define initial and final states

Specify input symbols

Build the transition table

Test input strings

🧩 Example Usage
Enter the number of states: 3
Enter 1 state: q0
Enter 2 state: q1
Enter 3 state: q2
...
Enter your String: 0101
Trace: q0 --0--> q1 --1--> q2 --0--> q1 --1--> q2
The string is ACCEPTED ✅ (ended in q2)
