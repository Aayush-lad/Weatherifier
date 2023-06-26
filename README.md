# Weatherifier

Weatherifier is a command-line tool that provides weather information for a specific city or geolocation. It utilizes the OpenWeatherMap API to fetch weather data and offers various functionalities such as displaying current weather, 5-day weather forecast, generating weather reports, translating weather descriptions, analyzing sentiment of weather-related comments, and converting weather reports to audio.

## Installation

1. Clone the Weatherifier repository from GitHub:


2. Navigate to the project directory:

   ```
   cd weatherifier
   ```

3. Install the required dependencies using pip:

   ```
   pip install click requests colorama geocoder pyperclip matplotlib azure-cognitiveservices-speech azure-identity azure-keyvault-secrets azure-ai-textanalytics azure-ai-language-conversations azure-ai-translation-text art

   ```



4. Run the Weatherifier tool:

   ```
   python weatherifier.py --help
   ```

## Usage

The Weatherifier tool supports the following command-line options:

- `--city`, `-c`: Display weather for a specific city.
- `--forecast`, `-f`: Display 5-day weather forecast and plot the graph.
- `--geolocation`, `-g`: Get weather based on geolocation.
- `--share`, `-s`: Share the weather report by copying it to the clipboard.
- `--tts`, `-t`: Convert the weather report to audio.
- `--comment`, `-cm`: Analyze sentiment of a weather-related comment.
- `--translate`, `-tr`: Translate weather description to a specific language.

**Note:** At least one option must be provided.

### Examples

1. Get weather for a specific city:

   ```
   python weatherifier.py -c Chennai
   ```

2. Get weather based on geolocation:

   ```
   python weatherifier.py -g
   ```

3. Display 5-day weather forecast and plot the graph:

   ```
   python weatherifier.py -c Chennai -f
   ```
   ![image](https://github.com/Fastest-Coder-First/Weatherifier/assets/126383391/3cfdf2fa-bab5-45d2-a80d-215cf5b16d9f)


4. Share the weather report for a specific city:

   ```
   python weatherifier.py -c Berlin -s
   ```

5. Convert the weather report for a specific city to audio:

   ```
   python weatherifier.py -c Chennai -t
   ```

6. Analyze sentiment of a weather-related comment:

   ```
   python weatherifier.py --comment "I love sunny days!"
   ```
![image](https://github.com/Fastest-Coder-First/Weatherifier/assets/126383391/f6484a46-dc97-409a-8515-9acb4be0adfa)

7. Translate weather description to a specific language:

   ```
   python weatherifier.py -c Madrid --translate fr
   ```
  ![image](https://github.com/Fastest-Coder-First/Weatherifier/assets/126383391/b2a1a505-e574-4578-93d2-fc08249bed2e)
 
## technologies used
Technologies Used
The Weatherifier command-line tool utilizes the following technologies and libraries:
### Github copilot
1.Increased Development Speed: With GitHub Copilot, I was able to write code faster and more efficiently. The AI-powered model suggests code based on the desired functionality, helping to accelerate the development process and reducing the cognitive load of manually writing every line of code.

2. Improved Code Quality: GitHub Copilot suggests code based on existing patterns and best practices, which can help improve the overall code quality of the Weatherifier project. It can prevent common errors, recommend appropriate code structures, and adhere to coding conventions.

3.Code Suggestion and Autocompletion: GitHub Copilot can assisted me by providing intelligent code suggestions and autocompletion while writing code for the Weatherifier project. It analyzes the context and provides relevant code snippets, reducing the time and effort required to write repetitive or boilerplate code.

Python: The programming language used to develop the tool.

OpenWeatherMap API: Provides weather data and forecasts for various locations worldwide.

Azure Cognitive Services: A collection of cloud-based APIs and services that enable developers to integrate AI capabilities into their applications. The following services are used:

Azure Translator Text API: Offers translation services to translate weather descriptions to different languages.

Azure Text Analytics API: Provides sentiment analysis capabilities to analyze the sentiment of weather-related comments.

Azure Conversation Analysis API: Enables analyzing conversational data to understand customer intents and insights.

Click: A Python package for creating command-line interfaces. It simplifies the process of defining and building command-line applications.

Colorama: A Python library that allows printing colored text and styling in the terminal. It enhances the visual presentation of the weather data.

Geocoder: A Python library that provides geocoding functionalities, allowing the tool to retrieve location information based on IP address.

Art: A Python library that enables ASCII art printing. It is used to display a stylized "Weatherifier" title at the beginning of the tool.

Pyperclip: A cross-platform Python module that provides a simple clipboard interface. It is used for copying the weather report to the clipboard for easy sharing.

Matplotlib: A Python plotting library that is used to visualize the 5-day weather forecast as a line graph.

Azure Speech SDK: The Microsoft Cognitive Services Speech SDK is utilized to convert weather reports into audio. It provides text-to-speech capabilities using different voices and languages.

These technologies and APIs come together to create a feature-rich command-line tool that provides weather information, generates reports, performs sentiment analysis, translates text, and converts text to speech.
# DEMO LINK
(https://drive.google.com/file/d/135O-i569IoZ61nj2d2rmmV0Xt_qOIB_5/view?usp=sharing)
## Acknowledgements
- Github copilot: helped in writing boilerplate code and  fetching api and documentation
- [OpenWeatherMap](https://openweathermap.org/): Provides the weather data API.
- [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/translator-text/): Offers the Translator Text API for language translation.
- [Geocoder](https://geocoder.readthedocs.io/): Python library for geocoding based on IP address.
- [Click](https://click.palletsprojects.com/): Python package for creating command-line interfaces.
- [Colorama](https://pypi.org/project/colorama/): Cross-platform package for colored terminal text.
