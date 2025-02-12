from __future__ import annotations

import logging
import os


def convert_container(
    path_file_video_origin: str, path_file_video_dest: str, flags: dict = {}
) -> None:
    """Make release for mp4 H264/AAC changing container without re-encode.

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
    """

    logging.info(
        "Convert video extension without reencode: %s", path_file_video_origin
    )

    stringa = (
        f'ffmpeg -v quiet -stats -y -i "{path_file_video_origin}" '
        + "-map_metadata -1 "
        + "-vcodec copy "
        + f'-acodec copy "{path_file_video_dest}"'
    )
    print(stringa)
    os.system(stringa)


def convert_only_audio(
    path_file_video_origin: str, path_file_video_dest: str, flags: dict = {}
) -> None:
    """Make release for mp4 H264/AAC converting only audio

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
    """

    logging.info("Convert only audio: %s", path_file_video_origin)

    stringa = (
        f'ffmpeg -v quiet -stats -y -i "{path_file_video_origin}" '
        + "-map_metadata -1 "
        + "-vcodec copy "
        + "-c:a aac "
        + "-ac 2 "
        + f'"{path_file_video_dest}"'
    )
    print("\n", stringa)
    os.system(stringa)


def convert_only_video_get_stringa(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> str:
    """get ffmpeg command to reencode a video as mp4 H264

    Args:
        path_file_video_origin (str): input video path
        path_file_video_dest (str): output video path
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.

    Returns:
        str: ffmpeg string command
    """

    crf = float(flags.get("crf", 18))
    maxrate = float(flags.get("maxrate", 4))
    bufsize = maxrate * 2
    stringa = (
        "ffmpeg -v quiet -stats -y "
        + f'-i "{path_file_video_origin}" '
        + "-map_metadata -1 "
        + "-c:v libx264 "
        + f"-crf {str(crf)} "
        + f"-maxrate {str(maxrate)}M "
        + f"-bufsize {str(bufsize)}M "
        + "-preset faster "
        + "-flags +global_header "
        + "-pix_fmt yuv420p "
        + "-profile:v baseline "
        + "-tune zerolatency "
        + "-movflags +faststart "
        + "-c:a copy "
        + f'"{path_file_video_dest}"'
    )
    return stringa


def convert_only_video(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> None:
    """Make release for mp4 H264/AAC converting only video

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.
    """

    logging.info("Convert only video: %s", path_file_video_origin)

    stringa = convert_only_video_get_stringa(
        path_file_video_origin, path_file_video_dest, flags
    )
    print("\n", stringa)
    os.system(stringa)


def convert_audio_video_get_stringa(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> str:
    """get ffmpeg command to convert a video as mp4 H264/AAC

    Args:
        path_file_video_origin (str): input video path
        path_file_video_dest (str): output video path
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.

    Returns:
        str: ffmpeg string command
    """

    crf = float(flags.get("crf", 18))
    maxrate = float(flags.get("maxrate", 4))
    bufsize = maxrate * 2
    stringa = (
        "ffmpeg -v quiet -stats -y "
        + f'-i "{path_file_video_origin}" '
        + "-map_metadata -1 "
        + "-c:v libx264 "
        + f"-crf {str(crf)} "
        + f"-maxrate {str(maxrate)}M "
        + f"-bufsize {str(bufsize)}M "
        + "-preset faster "
        + "-flags +global_header "
        + "-pix_fmt yuv420p "
        + "-profile:v baseline "
        + "-tune zerolatency "
        + "-movflags +faststart "
        + "-c:a aac "
        + "-ac 2 "
        + f'"{path_file_video_dest}"'
    )
    return stringa


def convert_audio_video(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> None:
    """Make release for mp4 H264/AAC converting audio and video

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.
    """

    stringa = convert_audio_video_get_stringa(
        path_file_video_origin, path_file_video_dest, flags
    )
    print("\n", stringa)
    os.system(stringa)
