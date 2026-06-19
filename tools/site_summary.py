import json
import os

SITE_DATA = {
    "name": "MK体育资讯站",
    "url": "https://ssl-cn-mk.com",
    "keywords": ["mk体育", "体育新闻", "赛事报道", "运动资讯"],
    "description": "提供最新最全的体育赛事报道、运动资讯与深度分析，涵盖国内外重大体育事件。",
    "tags": ["体育", "资讯", "新闻", "赛事"],
    "sections": [
        {"title": "足球", "summary": "国内外足球联赛、杯赛及国家队赛事即时报道"},
        {"title": "篮球", "summary": "NBA、CBA等篮球赛事比分、赛程与球员动态"},
        {"title": "网球", "summary": "ATP、WTA巡回赛及大满贯赛事直播与回顾"},
        {"title": "电子竞技", "summary": "热门电竞赛事、战队动态与行业解析"},
    ],
    "features": [
        "实时比分更新",
        "深度赛事分析",
        "多语言支持",
        "用户评论互动",
    ]
}

def format_banner(text: str, width: int = 60) -> str:
    border = "=" * width
    centered = text.center(width)
    return f"{border}\n{centered}\n{border}"

def generate_summary(data: dict) -> str:
    lines = []
    lines.append(format_banner("站点摘要报告"))
    lines.append("")
    lines.append(f"站点名称: {data['name']}")
    lines.append(f"主站地址: {data['url']}")
    lines.append(f"简短描述: {data['description']}")
    lines.append("")
    lines.append("核心关键词:")
    for kw in data["keywords"]:
        lines.append(f"  - {kw}")
    lines.append("")
    lines.append("内容标签:")
    for tag in data["tags"]:
        lines.append(f"  - {tag}")
    lines.append("")
    lines.append("内容板块:")
    for sec in data["sections"]:
        lines.append(f"  [{sec['title']}] {sec['summary']}")
    lines.append("")
    lines.append("平台特色:")
    for feat in data["features"]:
        lines.append(f"  * {feat}")
    lines.append("")
    lines.append(format_banner("摘要结束"))
    return "\n".join(lines)

def save_report(data: dict, output_dir: str = ".") -> str:
    summary = generate_summary(data)
    filename = "site_summary_report.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary)
    return filepath

def load_and_merge_extra_data(data: dict, extra_path: str = "extra_site_data.json") -> dict:
    merged = data.copy()
    if os.path.exists(extra_path):
        with open(extra_path, "r", encoding="utf-8") as f:
            extra = json.load(f)
        if isinstance(extra, dict):
            for key in extra:
                if key in merged:
                    if isinstance(merged[key], list) and isinstance(extra[key], list):
                        merged[key] = list(set(merged[key] + extra[key]))
                    else:
                        merged[key] = extra[key]
                else:
                    merged[key] = extra[key]
    return merged

def main():
    site = SITE_DATA
    site = load_and_merge_extra_data(site)
    report_path = save_report(site)
    print(f"摘要文件已生成: {report_path}")
    print(generate_summary(site))

if __name__ == "__main__":
    main()