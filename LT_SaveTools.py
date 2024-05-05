import re, sys
import xml.etree.ElementTree as ET

# HINT 基础功能
def create_node(tag, content, property_map={}):
    element = ET.Element(tag, property_map)
    element.text = content
    return element

# HINT 存档相关：修改奶牛设置
def edit_milk_setting(node_list):
    for node in node_list:
        if node.find('character/slavery/owner').attrib['value'] == 'PlayerCharacter':
            for sub_job in node.findall('character/slavery/slaveJobSettings/jobSetting'):
                if sub_job.attrib['job'] == 'MILKING':
                    for milk_item in sub_job.findall('setting'):
                        sub_job.remove(milk_item)
                    sub_job.append(create_node('setting', 'MILKING_MILK_CROTCH_AUTO_SELL'))
                    sub_job.append(create_node('setting', 'MILKING_MILK'))
                    sub_job.append(create_node('setting', 'MILKING_CUM_AUTO_SELL'))
                    sub_job.append(create_node('setting', 'MILKING_ARTISAN'))
                    sub_job.append(create_node('setting', 'MILKING_GIRLCUM_AUTO_SELL'))
                    sub_job.append(create_node('setting', 'MILKING_MILK_AUTO_SELL'))
                    sub_job.append(create_node('setting', 'MILKING_MILK_CROTCH'))
                    sub_job.append(create_node('setting', 'MILKING_CUM'))
                    sub_job.append(create_node('setting', 'MILKING_GIRLCUM'))
                    print('Milk Setting Changed')
# HINT 存档相关：修改奴隶权限设置


if __name__ == '__main__':
    xml_path = r'E:\@Joy\@Butter\@#Liliths Throne\data\saves\Test.xml'
    tree = ET.parse(xml_path)
    root = tree.getroot()
    npc_list = root.findall('NPC')
    edit_milk_setting(npc_list)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

# NOTE 2024-05-06 00:04:18 奴隶权限
'''<slavePermissionSettings>
          <permission type="GENERAL">
            <setting value="GENERAL_HOUSE_FREEDOM"/>
          </permission>
          <permission type="EXERCISE">
            <setting value="EXERCISE_NORMAL"/>
          </permission>
          <permission type="PREGNANCY">
            <setting value="PREGNANCY_ALLOW_EGG_LAYING"/>
            <setting value="PREGNANCY_ALLOW_BIRTHING"/>
          </permission>
          <permission type="BEHAVIOUR">
            <setting value="BEHAVIOUR_STANDARD"/>
          </permission>
          <permission type="SEX">
            <setting value="SEX_SAVE_VIRGINITY"/>
            <setting value="SEX_IMPREGNATED"/>
            <setting value="SEX_RECEIVE_SLAVES"/>
          </permission>
          <permission type="CLEANLINESS">
            <setting value="CLEANLINESS_WASH_CLOTHES"/>
            <setting value="CLEANLINESS_WASH_BODY"/>
          </permission>
          <permission type="PILLS">
            <setting value="PILLS_NO_PILLS"/>
          </permission>
          <permission type="DIET">
            <setting value="FOOD_NORMAL"/>
          </permission>
          <permission type="SLEEPING">
            <setting value="SLEEPING_DEFAULT"/>
          </permission>
        </slavePermissionSettings>'''