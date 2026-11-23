# Gaidant: One Founder, Connected Tools

QwenWork hackathon entry, Business Operations & Automation track. Gaidant is a one-person AI consultancy and software business; Cadence is its separate site-reporting product offering.

This repository contains public workflow prompts, architecture notes, a sanitised narration/edit plan and a portable full-frame video utility. It does **not** contain QwenWork, Hashmeta, Outlook, Canva or social-platform implementations, or the source of the deployed website or Cadence application.

## Demonstration Scope

- Website: recorded rendered Home, Consultancy, Cadence and contact pages. The business context describes an email-only contact route; no website-form-to-inbox handoff is established.
- Leads: a manually composed simulated enquiry and scheduled Outlook polling configuration, not an event-driven listener or an external customer lead.
- Reply: completed qualification summary, Outlook draft and a human clicking Send. Recipient delivery is not independently confirmed; no separate approval-system implementation is supplied.
- Marketing: visible Canva creative and a matching Instagram post. Intermediate API steps and approval history are not individually evidenced by the recording.
- Research: a completed briefing, not evidence of repeated unattended reliability.

These are separate demonstrations of connected work, not proof of one fully autonomous pipeline. Human review before customer-facing actions is the intended operating policy.

## Contents

- `docs/workflow-prompts.md`: reusable safe prompts and operating checklist.
- `docs/architecture.md`: boundaries, evidence and limitations.
- `docs/narration-edit-plan.md`: sanitised three-minute editorial plan.
- `scripts/build_video.py`: fit a privacy-reviewed input into a 1920x1080 canvas without cropping, mute source audio and refuse output overwrite.
- `tests/test_build_video.py`: synthetic-media checks only.

## Portable Video Utility

Requires Python 3.10+ and FFmpeg on PATH, or an explicit `--ffmpeg` executable. No third-party Python modules required.

```sh
python scripts/build_video.py reviewed-input.mp4 demo-output.mp4 --privacy-reviewed
python -m unittest discover -s tests -v
```

The utility is not a reconstruction of the private 180-second assembly. It preserves source duration, fits the complete image with letterboxing/pillarboxing, and outputs silent H.264 video. It performs no automatic privacy detection, redaction, narration, titles or publication. Review every source frame first; full-frame fitting can expose material a crop previously hid.

Raw recordings, generated media, personal email addresses, account/project IDs, connector settings, credentials and machine-specific paths are intentionally excluded. Originals remain private and untouched. No deployment or QW Page publishing is performed by these files.
