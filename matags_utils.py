import win32com.client

class OutlookConnectError(Exception):
    pass

class Matags(object):
    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
    except Exception as e:
        raise OutlookConnectError("Outlook not connected")

    # http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartClientCom.html
    selected = outlook.ActiveExplorer().Selection
    tags_str = clip.paste()
    tags = set(tags_str.split(", "))
    for item in selected:
        # print(item.Subject, item.To, tags_str)
        old_tags=set(item.Categories.split(', '))
        new_tags = old_tags|tags
        new_tags_str = ', '.join(new_tags)
        item.Categories = new_tags_str
        item.Save()

    def __init__(self):
        pass

    def extract(self):
        """
        extract tags,
        all the tags from selected messages will be extracted
        """
        selected = outlook.ActiveExplorer().Selection
        tags = set()
        for item in selected:
            # print(item.Subject, item.To, tags_str)
            _tags=self._str_to_tags(item.Categories)
            tags = tags|_tags
        return self._tags_to_str(tags)

    def set(self, tags_str):
        """
        set tags,
        existing tags will be removed
        """
        selected = outlook.ActiveExplorer().Selection
        for item in selected:
            item.Categories = tags_str
            item.Save()

    def append(self, tags_str):
        """
        append tags,
        existing tags will be staying there
        """
        _tags = self._str_to_tags(tags_str)
        selected = outlook.ActiveExplorer().Selection
        for item in selected:
            # print(item.Subject, item.To, tags_str)
            old_tags = self._str_to_tags(item.Categories)
            new_tags = old_tags|_tags
            new_tags_str = self._tags_to_str(new_tags)
            item.Categories = new_tags_str
            item.Save()       
    
    def _tags_to_str(self, tags):
        return ','.join(tags)

    def _str_to_tags(self, tag_str):
        if "," in tag_str:
            tags = set(tag.strip() for tag in tag_str.split(','))
        else:
            tags = set(tag.strip() for tag in tag_str.split())
        return tags      