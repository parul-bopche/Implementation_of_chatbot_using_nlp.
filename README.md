---

# Symptom Checker using NLP

## Overview

**Symptom Checker** is an intelligent application designed to help users identify possible health conditions based on their reported symptoms. By utilizing Natural Language Processing (NLP), it analyzes user inputs and matches them to a dataset of symptoms and related conditions. The app provides informative responses and guidance on when to seek medical attention.

## Features

- **User-Friendly Interface**: Easy-to-use design for seamless interaction.
- **NLP Integration**: Utilizes NLP to process and understand symptoms effectively.
- **Comprehensive Dataset**: Includes a wide range of symptoms and conditions for accurate matching.
- **Response Generation**: Offers tailored advice based on symptoms.
- **Ongoing Updates**: Continuously updated to include new symptoms and conditions.

## Dataset

The app uses a JSON dataset (`symptoms.json`) that includes:

- **Tags**: Labels for each health condition.
- **Patterns**: Common symptoms or phrases users may report.
- **Responses**: Helpful guidance based on the reported symptoms.

### Example Entry

```json
{
  "tag": "migraine",
  "patterns": [
    "I have a severe headache",
    "My head hurts a lot",
    "I feel nauseous with my headache"
  ],
  "responses": [
    "These symptoms may indicate a migraine. Consider resting in a dark room and staying hydrated.",
    "If headaches persist or worsen, consult a healthcare provider."
  ]
}
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sandesh13fr/symptom_checker.git
   ```
2. Navigate to the project folder:
   ```bash
   cd symptom_checker
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Input your symptoms as prompted.
3. Receive feedback and advice based on your input.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the developers of the NLP libraries used in this project.
- Special recognition to the Edunet Foundation team for their support.

---

This version keeps the content concise and removes external links. Let me know if you'd like to make further adjustments!
