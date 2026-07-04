from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ResearchItem:
    subreddit: str
    title: str
    selftext: str
    ups: int
    num_comments: int
    url: str
    image_url: Optional[str] = None

@dataclass
class NewsArticle:
    source: str
    title: str
    description: str
    pubDate: str
    url: str

@dataclass
class ContentIdea:
    id: str
    topic: str
    prompt: str
    output_text: Optional[str] = None

@dataclass
class CarouselSlide:
    slide_num: int
    header_label: str = ""
    hook_part_1: str = ""
    hook_part_2: str = ""
    hook_emphasis: str = ""
    subtitle: str = ""
    pill_label: str = ""
    eyebrow: str = ""
    headline_part_1: str = ""
    headline_part_2: str = ""
    headline_emphasis: str = ""
    subhead: str = ""
    body_text: str = ""
    huge_stat: str = ""
    circle_word_1: str = ""
    circle_word_2: str = ""

@dataclass
class Carousel:
    caption: str
    slides: List[CarouselSlide] = field(default_factory=list)

@dataclass
class InfographicBar:
    label: str
    value: str
    color: str

@dataclass
class Infographic:
    title_main: str
    title_span: str
    subtitle: str
    badge: str
    date_label: str
    takeaway_num: str
    takeaway_text: str
    source: str
    bars: List[InfographicBar] = field(default_factory=list)

@dataclass
class Asset:
    file_path: str
    file_type: str  # 'pdf' or 'png'
    file_name: str

@dataclass
class PublishJob:
    post_id: str
    text_content: str
    assets: List[Asset] = field(default_factory=list)
    scheduled_time: Optional[str] = None
