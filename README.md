Synthetic Fraud Data Using CTGAN
This repository provides tools and code to generate synthetic fraud datasets using the CTGAN (Conditional Generative Adversarial Network) model. Synthetic data is useful for testing fraud detection algorithms when real-world data is limited or sensitive.

Features
Generate synthetic tabular data similar to real-world fraud datasets
Use CTGAN for high-fidelity data synthesis
Example code for data preprocessing, training, and generation
Installation
Clone the repository:

bash
git clone https://github.com/ayushsri/Synthetic-Fraud-Data-Using-CTGAN.git
cd Synthetic-Fraud-Data-Using-CTGAN
Install dependencies:

bash
pip install -r requirements.txt
Usage
Prepare your real dataset in CSV format.

Edit the configuration or script to point to your dataset.

Run the main script to train CTGAN and generate synthetic data:

bash
python main.py
Generated synthetic data will be saved to the specified output path.

Project Structure
Code
.
├── data/             # Real and synthetic datasets
├── main.py           # Main script to run CTGAN
├── utils.py          # Utility functions
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
Requirements
Python 3.7+
ctgan
pandas
numpy
(See requirements.txt for complete list.)

References
CTGAN Paper
CTGAN GitHub
License
This project is licensed under the MIT License.

Let me know if you want sections on contributing, FAQ, or examples for specific scripts!
