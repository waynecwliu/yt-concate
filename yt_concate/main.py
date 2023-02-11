from yt_concate.pipeline.steps.get_vedio_list import GetVedioList
from yt_concate.pipeline.steps.step import StepException

from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
        }

    steps = [
        GetVedioList(),
        # 擴充性
        ]


    p = Pipeline(steps)     # pipeline design pattern
    p.run(inputs)

if __name__ == '__main__':      # 檢查此檔案是否為進入點
    main()




# vedio_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(vedio_list))
