# Zhang Xuefeng

张雪峰内容的独立转录仓库，来源为 Bilibili 空间：

- `https://space.bilibili.com/28152637/video`

## 目录

- `scripts/transcribe_bili.py`：逐视频发现、下载、转录、校验并提交状态
- `scripts/transcription_integrity.py`：音频与转录完整性检查
- `transcripts/`：转录文本
- `state/`：队列、完成/失败状态和进度
- `.github/workflows/transcribe.yml`：手动或每 6 小时运行一次，每次处理一个视频并按 `continue.flag` 串行续跑
- `.github/workflows/retry_failed_transcripts.yml`：失败项重试入口

## GitHub Secret

在本仓库配置 `BILIBILI_COOKIES`。Cookie 只通过 Actions Secret 注入，不写入仓库。

## 兼容迁移说明

本仓库从 `Business-Unit-for-Video/Video2Text` 独立出来，保留了原有 `transcripts/` 和 `state/` 路径以及历史状态，避免已经完成的视频被重复处理。原 `Video2Text` 仓库暂不清理，待本仓库验证后再单独处理。

## 运行原则

- 一个 Run 只处理一个视频。
- 成功后才提交状态，并在存在 `continue.flag` 时触发下一个 Run。
- 不打印 Cookie，不把媒体临时文件提交到 Git。
- 请确保源内容具有相应的授权、许可或其他合法使用依据。
