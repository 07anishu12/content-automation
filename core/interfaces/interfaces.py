from abc import ABC, abstractmethod
from typing import List
from core.models.models import ResearchItem, NewsArticle, ContentIdea, PublishJob, Asset

class ResearchProvider(ABC):
    @abstractmethod
    def fetch_reddit_posts(self) -> List[ResearchItem]:
        pass

    @abstractmethod
    def fetch_news_articles(self) -> List[NewsArticle]:
        pass

class ContentGenerator(ABC):
    @abstractmethod
    def generate_posts(self, feeds: List[ResearchItem], news: List[NewsArticle]) -> List[ContentIdea]:
        pass

class AssetGenerator(ABC):
    @abstractmethod
    def generate_carousel_pdf(self, carousel_data) -> Asset:
        pass

    @abstractmethod
    def generate_infographic_png(self, infographic_data) -> Asset:
        pass

class Publisher(ABC):
    @abstractmethod
    def publish_slack(self, job: PublishJob) -> bool:
        pass

class Scheduler(ABC):
    @abstractmethod
    def schedule_posts(self, jobs: List[PublishJob]) -> bool:
        pass
