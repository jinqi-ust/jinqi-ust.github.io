# Jin Qi 个人学术主页

英文静态网站，适合发布到 GitHub Pages。执行下面的构建命令后，双击 `dist/index.html` 即可查看；无需安装前端依赖。

包含个人介绍、研究方向、25 篇论文及工作论文、研究团队、学术经历、研究项目、教学和获奖。团队名单来自 2026 年 8 月 CV：8 位在读学生、2 位现任博士后、9 位博士毕业生、5 位 MPhil 毕业生、2 位往届博士后。部分成员同时出现在不同培养阶段，属于正常记录。

## 发布到当前 GitHub Pages

本网站部署到 [jinqi-ust.github.io](https://jinqi-ust.github.io/)。源码位于仓库的 `personal-website/` 文件夹。

修改资料后提交到 `main`，仓库根目录的 **Deploy site** 工作流会生成网页、检查内容及资源，并将结果发布到现有 `gh-pages` 分支。GitHub Pages 的来源继续使用 **Deploy from a branch → gh-pages → / (root)**，无需切换设置。合并前的更新请求只构建检查并保存预览文件，不会修改正式主页。

旧版 al-folio 的源文件与 Git 历史保留在仓库中。恢复旧版时，可以从新版上线前的提交恢复旧发布工作流。已有 `/publications/`、`/grants/`、`/people/`、`/teaching/`、`/awards/` 地址会跳转到新版的对应内容；`/cv/` 会直接打开 CV PDF。

## 更新内容

| 想修改的内容                                 | 文件                 |
| -------------------------------------------- | -------------------- |
| 在读学生、博士后、毕业生、去向、团队资料日期 | `data/people.json`   |
| 论文、项目、教学、获奖、教育和任职           | `data/academic.json` |
| 个人介绍、联系方式、外部链接                 | `template.html`      |
| 配色、字号、页面布局                         | `assets/style.css`   |
| 个人照片                                     | `assets/jin-qi.jpg`  |

`academic.json` 每篇论文的 `student_postdoc_authors` 列出需要加 `*` 的作者姓名，表示研究启动时为博士生或博士后；`alphabetical_order: true` 会在论文编号后加 `†`，表示按字母顺序署名、贡献相同。这些标记逐篇对应原始 Word CV，不根据当前学生名单推断。

`people.json` 中每个人都独立成条目，可以直接修改姓名、时间、共同指导说明和职位。`as_of` 是名单核对日期。`academic.json` 的 `updated` 是网站资料更新时间，`as_of` 是学术资料来源日期。

使用完整源码及 GitHub Actions 时，修改这些文件后提交即可自动发布。在本地更新时，用 Python 3.10 或以上版本执行：

```bash
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

然后访问 `http://127.0.0.1:8765/`。直接编辑 `dist/index.html` 也能改网页，但下次生成会覆盖，所以建议修改资料文件和模板。

## 资料口径

- 个人身份、研究主题、联系方式和照片参照 [HKUST 院系主页](https://www.ieda.ust.hk/eng/faculty-staff.php?catid=5&sid=15&id=22)。
- 团队信息，以及论文题名、作者顺序、状态和课程年份，以用户提供的 `CV_Jin QI_202608.docx` 为准。名单及毕业去向标注为 August 2026，没有推测其后的变化。
- 全部论文题名、作者、研究项目等存于 JSON，可继续人工修订；未编造论文 DOI、学生网站或照片。
- 主页的 `CV` 按钮直接打开 `assets/CV_Jin_Qi.pdf`，可在浏览器中查看或下载。PDF 使用与原 Word 同目录的 `CV_Jin QI_202608.pdf`，已核对其内容与 Word 一致，保留原排版。
- 经用户授权，完整 CV PDF 已包含在项目中；原始 DOCX 未上传。更新 CV 时替换 `assets/CV_Jin_Qi.pdf`，网址保持不变。
- 页面补充的 2005 年团体射击比赛奖项来自院系主页。

院系网页与 CV 存在一些差异，已按 CV 整理：

- 乘客等待行为和服务网络设计论文的题名，以及 fragility-aware classification 稿件的作者顺序。
- 水资源基础设施规划论文在 CV 中为 Naval Research Logistics 的 major revision；网页为 under review。
- IEDA3230 的起始年份在 CV 中为 2022，网页为 2023；物流课程代码采用 CV 中的 IELM2410。
- 个别项目名称及截止年份采用 CV，例如 auction design 至 2025、Early Career Scheme 至 2020。

发布流程参考 [创建 GitHub Pages 网站](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) 与 [GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。
