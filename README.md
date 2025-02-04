# YouTube Channel Notifier

A simple Tkinter-based desktop application that notifies users about the latest videos uploaded on selected YouTube channels. The app uses the YouTube Data API to fetch the status of the latest video uploads.

## Features

- Displays a list of YouTube channels.
- Shows the status of the latest video from a selected channel (1 for a new video, 0 for no new video).
- Easy-to-use graphical interface built with Tkinter.

## Prerequisites

- Python 3.x
- You will need a Google API key to access the YouTube Data API.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Install the required Python packages:

    ```bash
    pip install google-api-python-client
    ```

3. Replace `'KEY'` in the `YOUTUBE_API_KEY` variable in the script with your YouTube API key.

4. Run the script:

    ```bash
    python youtube_notifier.py
    ```

## How It Works

- The application displays a list of YouTube channels.
- When a channel is selected, it fetches the latest video from the channel and displays whether there is a new upload.
- If there is a new video, it will show "1", otherwise it shows "0".
- In case of an error, the app will notify you with an error message.

## Customizing Channels

To add more channels, modify the `load_channels` method by adding the respective channel IDs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
