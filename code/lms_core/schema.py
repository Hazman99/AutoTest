from ninja import Schema, Field

from typing import Optional
from datetime import datetime
from ninja import FilterSchema
from django.db.models import Q

from django.contrib.auth.models import User

class UserOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str


class CourseSchemaOut(Schema):
    id: int
    name: str
    description: str
    price: int
    image : Optional[str]
    teacher: UserOut
    created_at: datetime
    updated_at: datetime

class CourseMemberOut(Schema):
    id: int 
    course_id: CourseSchemaOut
    user_id: UserOut
    roles: str
    # created_at: datetime


class CourseSchemaIn(Schema):
    name: str
    description: str
    price: int


class CourseContentMini(Schema):
    id: int
    name: str
    description: str
    course_id: CourseSchemaOut
    created_at: datetime
    updated_at: datetime


class CourseContentFull(Schema):
    id: int
    name: str
    description: str
    video_url: Optional[str]
    file_attachment: Optional[str]
    course_id: CourseSchemaOut
    created_at: datetime
    updated_at: datetime

class CourseCommentOut(Schema):
    id: int
    content_id: CourseContentMini
    member_id: CourseMemberOut
    comment: str
    created_at: datetime
    updated_at: datetime

class CourseCommentIn(Schema):
    comment: str


class CourseFilter(FilterSchema):
    price_gte: Optional[int] = 0
    price_lte: Optional[int] = 0
    created_gte: Optional[datetime] = None
    created_lte: Optional[datetime] = None
    search : Optional[str] = Field(None, q=['name__icontains', 'description__icontains'])

    def filter_price_gte(self, value: int):
        return Q(price__gte=value) if value else Q()
    
    def filter_price_lte(self, value: int):
        return Q(price__lte=value) if value else Q()
    
    def filter_created_gte(self, value: datetime):
        return Q(created_at__gte=value) if value else Q()
    
    def filter_created_lte(self, value: datetime):        
        return Q(created_at__lte=value) if value else Q()
    

class HelloResponse(Schema):
    msg: str