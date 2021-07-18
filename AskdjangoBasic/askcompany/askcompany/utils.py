import os
from uuid import uuid4
from django.utils import timezone

def uuid_upload_to(instance, filename):
    #app_label = instance.__class__._meta.app_label # 앱 별로
    #cls_name = instance.__class__.__name__.lower() # 모델 별로
    #ymd_path = timezone.now().strftime('%Y/%m/%d’) # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
    return '/'.join([
        #app_label,
        #cls_name,
        #ymd_path,
        uuid_name[:2], #256가지 조합
        uuid_name[2:4],
        uuid_name[4:] + ext,
    ])