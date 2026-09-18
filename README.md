# iKala 競品雷達 — Vercel 部署資料夾

## 檔案結構
- `source.html` —— 內容來源（唯一真相）。跟 Claude Artifact 上發布的那份完全同步。
- `build.py` —— 把 `source.html` 包成完整的 `index.html`（Artifact 版是片段檔，沒有 `<html>/<head>/<body>`，Vercel 部署需要完整文件）。
- `index.html` —— 實際部署到 Vercel 的檔案，由 `build.py` 自動產生，**不要手改這個檔案**，改了也會在下次 build 時被覆蓋。

## 兩個版本的差異
| | Claude Artifact | Vercel 部署 |
|---|---|---|
| 網址 | claude.ai/code/artifact/57b6a9b9-... | 你的 Vercel 網址 |
| 資料來源 | 連即時資料庫，Claude 更新資料後**自動**反映 | 開頁當下嵌入的**靜態快照**，資料不會自動更新 |
| 適合場合 | 你自己或 Claude 查資料時用 | 分享給主管、不需要即時性的場合 |

**重要**：Vercel 版是快照。之後 Claude 幫你在 Artifact 上更新競品資料後，Vercel 版不會自動跟著變，要重新 build + 重新部署才會同步。想更新 Vercel 版時，直接跟 Claude 說「幫我把競品雷達重新部署」。

## 如何更新並重新部署
1. 請 Claude 修改 `source.html`（或請 Claude 直接處理，不用自己動手）。
2. 跑 `python3 build.py` 重新產生 `index.html`。
3. 在這個資料夾執行 `npx vercel --prod` 重新部署（第一次要先 `npx vercel login`）。

## 功能
- 篩選：AI Service／AI Marketing 分組、7／30／90 天／半年範圍、六種訊號分類。
- 匯出：篩選列下方「匯出 HTML」「匯出 PDF」按鈕，會依照**當下畫面上的篩選狀態**匯出（HTML 是可另外分享的獨立快照檔；PDF 走瀏覽器列印，另存為 PDF 即可）。

<!-- git 自動部署測試 2026-09-18T06:50:04Z -->
