#!/usr/bin/env python3
"""
把 source.html（給 Claude Artifact 用的片段檔，沒有 <!doctype>/<html>/<head>/<body>）
包成 index.html（給 Vercel 部署用的完整 HTML 文件）。

用法：
    python3 build.py

source.html 是唯一的內容來源。要更新 dashboard，改 source.html，
然後跑這支腳本重新產生 index.html，再用 vercel --prod 重新部署。
"""
import re
import pathlib

HERE = pathlib.Path(__file__).parent
src = (HERE / "source.html").read_text(encoding="utf-8")

title_m = re.search(r"<title>(.*?)</title>", src)
title = title_m.group(0)
rest = src[title_m.end():]

wrapped = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{title}
{rest}
</html>
"""

(HERE / "index.html").write_text(wrapped, encoding="utf-8")
print(f"wrote index.html ({len(wrapped)} bytes)")
