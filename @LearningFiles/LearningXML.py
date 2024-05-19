# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
# Author Start
# hint Date: 2024-05-06 00:04:18
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2024-05-06 00:04:18
# hint Description:
# hint FilePath: \PythonSmallTools\LearningXML.py
# Author End

import xml.etree.ElementTree as ET

# TODO 修改文件修改库，换成lxml库 https://www.cnblogs.com/iamdongyang/p/11765782.html

# HINT 基础功能
def create_node(tag, content, property_map={}):
    element = ET.Element(tag, property_map)
    element.text = content
    return element


# HINT 存档相关：修改奶牛设置
def edit_milk_setting(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            for sub_job in node.findall(
                "character/slavery/slaveJobSettings/jobSetting"
            ):
                if sub_job.attrib["job"] == "MILKING":
                    for milk_item in sub_job.findall("setting"):
                        sub_job.remove(milk_item)
                    sub_job.append(
                        create_node("setting", "MILKING_MILK_CROTCH_AUTO_SELL")
                    )
                    sub_job.append(create_node("setting", "MILKING_MILK"))
                    sub_job.append(create_node("setting", "MILKING_CUM_AUTO_SELL"))
                    sub_job.append(create_node("setting", "MILKING_ARTISAN"))
                    sub_job.append(create_node("setting", "MILKING_GIRLCUM_AUTO_SELL"))
                    sub_job.append(create_node("setting", "MILKING_MILK_AUTO_SELL"))
                    sub_job.append(create_node("setting", "MILKING_MILK_CROTCH"))
                    sub_job.append(create_node("setting", "MILKING_CUM"))
                    sub_job.append(create_node("setting", "MILKING_GIRLCUM"))

                    edit_count += 1
    print(f"Milk Setting {edit_count} Changed")


# HINT 存档相关：修改奴隶权限设置
def edit_slave_permission_settings(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            slavery = node.find("character/slavery")
            permission = node.find("character/slavery/slavePermissionSettings")
            slavery.remove(permission)
            permissions = ET.fromstring("""<slavePermissionSettings>    <permission type="GENERAL">        <setting value="GENERAL_HOUSE_FREEDOM" />    </permission>    <permission type="EXERCISE">        <setting value="EXERCISE_NORMAL" />    </permission>    <permission type="PREGNANCY">        <setting value="PREGNANCY_ALLOW_EGG_LAYING" />        <setting value="PREGNANCY_ALLOW_BIRTHING" />    </permission>    <permission type="BEHAVIOUR">        <setting value="BEHAVIOUR_STANDARD" />    </permission>    <permission type="SEX">        <setting value="SEX_SAVE_VIRGINITY" />        <setting value="SEX_IMPREGNATED" />        <setting value="SEX_RECEIVE_SLAVES" />    </permission>    <permission type="CLEANLINESS">        <setting value="CLEANLINESS_WASH_CLOTHES" />        <setting value="CLEANLINESS_WASH_BODY" />    </permission>    <permission type="PILLS">        <setting value="PILLS_NO_PILLS" />    </permission>    <permission type="DIET">        <setting value="FOOD_NORMAL" />    </permission>    <permission type="SLEEPING">        <setting value="SLEEPING_DEFAULT" />    </permission></slavePermissionSettings>""")
            slavery.append(permissions)
            edit_count += 1
    print(f"Slave Permission Setting {edit_count} Changed")

# HINT 修改奴隶的好感度与服从度
def edit_slave_obedience_(node_list):
    edit_count_o, edit_count_r, add_relation= 0, 0, 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":

            node.find("character/core/obedience").attrib["value"] = "100.0"
            edit_count_o += 1

            relationships = node.findall("character/characterRelationships/relationship")
            state_player = False
            for relationship in relationships:
                if relationship.attrib["character"] == "PlayerCharacter":
                    relationship.attrib["value"] = "100.0"
                    edit_count_r += 1
                    state_player = True
                    break
            if not state_player:
                base_relation = node.find("character/characterRelationships")
                player_relation = ET.fromstring("""<relationship character="PlayerCharacter" value="100.0" />""")
                base_relation.append(player_relation)
                add_relation += 1

    print(f"Obedience Setting {edit_count_o} Changed")
    print(f"Relationships Setting {edit_count_r} Changed, {add_relation} Added")

# HINT 修改奴隶的身体部位
def edit_slave_body_parts(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            # Change femininity
            node.find("character/body/bodyCore").attrib["femininity"] = "100"
            # Find Body
            body_part = node.find("character/body")
            # Anus Part
            body_part.remove(body_part.find("anus"))
            anus_node = ET.fromstring("""<anus assHair="ZERO_NONE" bleached="false" capacity="0.0" depth="7" elasticity="7" plasticity="0" stretchedCapacity="0.0" virgin="false" wetness="7"><mod>MUSCLE_CONTROL</mod><mod>PUFFY</mod><mod>RIBBED</mod><mod>TENTACLED</mod></anus>""")
            body_part.append(anus_node)
            # Breasts Part <breasts milkRegeneration="500000" milkStorage="10000" size="14" storedMilk="10000.0" />
            node.find("character/body/breasts").attrib["milkRegeneration"] = "500000"
            node.find("character/body/breasts").attrib["milkStorage"] = "10000"
            node.find("character/body/breasts").attrib["storedMilk"] = "10000.0"
            # Mouth Part <mouthcapacity="0.0"depth="7"elasticity="7"lipSize="3"piercedLip="false"plasticity="0"stretchedCapacity="0.0"virgin="false"wetness="7"><mod>MUSCLE_CONTROL</mod><mod>PUFFY</mod><mod>RIBBED</mod><mod>TENTACLED</mod></mouth>
            body_part.remove(body_part.find("mouth"))
            mouth_node = ET.fromstring("""<mouth capacity="0.0" depth="7" elasticity="7" lipSize="3" piercedLip="false" plasticity="0" stretchedCapacity="0.0" virgin="false" wetness="7"><mod>MUSCLE_CONTROL</mod><mod>PUFFY</mod><mod>RIBBED</mod><mod>TENTACLED</mod></mouth>""")
            body_part.append(mouth_node)

            # Vagina Part
            node.find("character/body/vagina").attrib["capacity"] = "0.0"
            node.find("character/body/vagina").attrib["depth"] = "7"
            node.find("character/body/vagina").attrib["elasticity"] = "7"
            node.find("character/body/vagina").attrib["wetness"] = "7"
            node.find("character/body/vagina").attrib["plasticity"] = "0"
            node.find("character/body/vagina").attrib["stretchedCapacity"] = "0.0"
            node.find("character/body/vagina").attrib["squirter"] = "true"
            vagina_mod_list = node.findall("character/body/vagina/mod")
            if len(vagina_mod_list)>0:
                for v_mod in vagina_mod_list:
                    node.find("character/body/vagina").remove(v_mod)
            # <mod>MUSCLE_CONTROL</mod> <mod>PUFFY</mod> <mod>RIBBED</mod> <mod>TENTACLED</mod>
            vagina_part = node.find("character/body/vagina")
            vagina_part.append(create_node("mod", "MUSCLE_CONTROL"))
            vagina_part.append(create_node("mod", "PUFFY"))
            vagina_part.append(create_node("mod", "RIBBED"))
            vagina_part.append(create_node("mod", "TENTACLED"))

            edit_count += 1
    print(f"Body Setting {edit_count} Changed")


if __name__ == "__main__":

    # xml_path = r"./TestDataset/Learning.xml"
    xml_path = r"E:\@Joy\@Butter\@#Liliths Throne\data\saves\AutoSave_乔茜.xml"
    # xml_path = r"E:\@Joy\@Butter\@#Liliths Throne\data\saves\Test.xml"
    tree = ET.parse(xml_path)
    root = tree.getroot()
    npc_list = root.findall("NPC")

    edit_milk_setting(npc_list)
    edit_slave_permission_settings(npc_list)
    edit_slave_obedience_(npc_list)
    edit_slave_body_parts(npc_list)

    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print("XML saved")