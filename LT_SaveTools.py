# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2024-05-05 23:53:52
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2024-05-06 19:23:24
# hint Description:
# hint FilePath: \PythonSmallTools\LT_SaveTools.py
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
            node.find("character/body/breastsCrotch").attrib["milkRegeneration"] = "500000"
            node.find("character/body/breastsCrotch").attrib["milkStorage"] = "10000"
            node.find("character/body/breastsCrotch").attrib["storedMilk"] = "10000.0"
            # Mouth Part
            body_part.remove(body_part.find("mouth"))
            mouth_node = ET.fromstring("""<mouth capacity="0.0" depth="7" elasticity="7" lipSize="3" piercedLip="false" plasticity="0" stretchedCapacity="0.0" virgin="false" wetness="7"><mod>MUSCLE_CONTROL</mod><mod>PUFFY</mod><mod>RIBBED</mod><mod>TENTACLED</mod></mouth>""")
            body_part.append(mouth_node)
            # penis Part
            node.find("character/body/penis").attrib["type"] = "NONE"
            node.find("character/body/penis").attrib["size"] = "0"
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
            vagina_part = node.find("character/body/vagina")
            vagina_part.append(create_node("mod", "MUSCLE_CONTROL"))
            vagina_part.append(create_node("mod", "PUFFY"))
            vagina_part.append(create_node("mod", "RIBBED"))
            vagina_part.append(create_node("mod", "TENTACLED"))
            # Milk Part
            milk_part = node.find("character/body/milk")
            milk_part.attrib["flavour"] = "MILK"
            milkCrotch_part = node.find("character/body/milkCrotch")
            milkCrotch_part.attrib["flavour"] = "MILK"
            milk_mod_list = milk_part.findall("mod")
            if milk_mod_list is not None:
                for milk_mod in milk_mod_list:
                    milk_part.remove(milk_mod)
            milkCrotch_mod_list = milkCrotch_part.findall("mod")
            if milkCrotch_mod_list is not None:
                for milkCrotch_mod in milkCrotch_mod_list:
                    milkCrotch_part.remove(milkCrotch_mod)
            milk_part.append(create_node("mod", "SLIMY"))
            milk_part.append(create_node("mod", "MUSKY"))
            milk_part.append(create_node("mod", "STICKY"))
            milkCrotch_part.append(create_node("mod", "SLIMY"))
            milkCrotch_part.append(create_node("mod", "MUSKY"))
            milkCrotch_part.append(create_node("mod", "STICKY"))
            # girlcum Part
            girlcum_part = node.find("character/body/girlcum")
            girlcum_part.attrib["flavour"] = "GIRL_CUM"
            girlcum_mod_list = girlcum_part.findall("mod")
            if girlcum_mod_list is not None:
                for girlcum_mod in girlcum_mod_list:
                    girlcum_mod_list.remove(girlcum_mod)
            girlcum_part.append(create_node("mod", "SLIMY"))
            girlcum_part.append(create_node("mod", "MUSKY"))
            # pierced part
            node.find("character/body/nipples").attrib["pierced"] = "true"
            node.find("character/body/ear").attrib["pierced"] = "true"
            node.find("character/body/nipplesCrotch").attrib["pierced"] = "true"
            node.find("character/body/vagina").attrib["pierced"] = "true"
            node.find("character/body/tongue").attrib["piercedTongue"] = "true"

            edit_count += 1
    print(f"Body Setting {edit_count} Changed")

# HINT 更改称谓 <fatherName value="乔茜"/>  <petNames><petNameEntry id="PlayerCharacter" petName="妈妈主人"/></petNames>
def edit_pet_name(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            if node.find("character/family/fatherId").attrib["value"] == "PlayerCharacter":
                for petNameEntry in node.findall("character/core/petNames/petNameEntry"):
                    if petNameEntry.attrib["id"] == "PlayerCharacter":
                        petNameEntry.attrib["petName"] = "妈妈"
                        edit_count += 1
                        break
            else:
                for petNameEntry in node.findall("character/core/petNames/petNameEntry"):
                    if petNameEntry.attrib["id"] == "PlayerCharacter":
                        petNameEntry.attrib["petName"] = "主人"
                        edit_count += 1
                        break

    print(f"Pet Name Setting {edit_count} Changed")

# HINT 变更法术
def edit_spell(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            knownSpells = node.find("character/knownSpells")
            if knownSpells is not None:
                node.find("character").remove(knownSpells)

            new_spells = ET.fromstring("""<knownSpells>    <spell type="ARCANE_AROUSAL"/>    <spell type="TELEPATHIC_COMMUNICATION"/>    <spell type="FIREBALL"/>    <spell type="ARCANE_CLOUD"/>    <spell type="FLASH"/>    <spell type="SOOTHING_WATERS"/>    <spell type="ELEMENTAL_ARCANE"/>    <spell type="CLOAK_OF_FLAMES"/>    <spell type="STONE_SHELL"/>    <spell type="ELEMENTAL_EARTH"/>    <spell type="TELEKENETIC_SHOWER"/>    <spell type="ELEMENTAL_FIRE"/></knownSpells>""")
            node.find("character").append(new_spells)

            spellUpgrades = node.find("character/spellUpgrades")
            if spellUpgrades is not None:
                node.find("character").remove(spellUpgrades)
            new_SU = ET.fromstring("""<spellUpgrades>    <upgrade type="FIREBALL_1"/>    <upgrade type="FIREBALL_2"/>    <upgrade type="FIREBALL_3"/>    <upgrade type="FLASH_1"/>    <upgrade type="FLASH_2"/>    <upgrade type="FLASH_3"/>    <upgrade type="CLOAK_OF_FLAMES_1"/>    <upgrade type="CLOAK_OF_FLAMES_2"/>    <upgrade type="CLOAK_OF_FLAMES_3"/>    <upgrade type="ELEMENTAL_FIRE_1"/>    <upgrade type="ELEMENTAL_FIRE_2"/>    <upgrade type="ELEMENTAL_FIRE_3B"/>    <upgrade type="SOOTHING_WATERS_1_CLEAN"/>    <upgrade type="SOOTHING_WATERS_2_CLEAN"/>    <upgrade type="SOOTHING_WATERS_1"/>    <upgrade type="SOOTHING_WATERS_2"/>    <upgrade type="SOOTHING_WATERS_3"/>    <upgrade type="TELEKENETIC_SHOWER_1"/>    <upgrade type="TELEKENETIC_SHOWER_2"/>    <upgrade type="TELEKENETIC_SHOWER_3"/>    <upgrade type="STONE_SHELL_1"/>    <upgrade type="STONE_SHELL_2"/>    <upgrade type="STONE_SHELL_3"/>    <upgrade type="ELEMENTAL_EARTH_1"/>    <upgrade type="ELEMENTAL_EARTH_2"/>    <upgrade type="ELEMENTAL_EARTH_3B"/>    <upgrade type="ARCANE_AROUSAL_1"/>    <upgrade type="ARCANE_AROUSAL_2"/>    <upgrade type="ARCANE_AROUSAL_3"/>    <upgrade type="TELEPATHIC_COMMUNICATION_1"/>    <upgrade type="TELEPATHIC_COMMUNICATION_2"/>    <upgrade type="TELEPATHIC_COMMUNICATION_3"/>    <upgrade type="ARCANE_CLOUD_1"/>    <upgrade type="ARCANE_CLOUD_2"/>    <upgrade type="ARCANE_CLOUD_3"/>    <upgrade type="ELEMENTAL_ARCANE_1"/>    <upgrade type="ELEMENTAL_ARCANE_2"/>    <upgrade type="ELEMENTAL_ARCANE_3B"/></spellUpgrades>""")
            node.find("character").append(new_SU)
            edit_count += 1
    print(f"Spell Setting {edit_count} Changed")

# HINT 刺青编辑
def edit_tattoo(node_list):
    edit_count = 0
    for node in node_list:
        if node.find("character/slavery/owner").attrib["value"] == "PlayerCharacter":
            tattoos = node.find("character/tattoos")
            if tattoos is not None:
                node.find("character").remove(tattoos)
            new_tattoos = ET.fromstring("""<tattoos>    <tattooEntry slot="ANUS">        <tattoo glowing="true" id="innoxia_hearts_hearts" name="心形" primaryColour="CLOTHING_PURPLE_ROYAL" secondaryColour="CLOTHING_PURPLE_ROYAL">            <tattooWriting colour="CLOTHING_PURPLE_ROYAL" glow="true"><![CDATA[内射我吧！]]>                <styles>                    <style value="ITALICISED"/>                    <style value="BOLD"/>                </styles>            </tattooWriting>            <tattooCounter colour="CLOTHING_PURPLE_ROYAL" countType="NUMBERS" glow="true" type="CUM_TAKEN"/>            <effects/>        </tattoo>    </tattooEntry>    <tattooEntry slot="GROIN">        <tattoo glowing="true" id="innoxia_heartWomb_heart_womb" name="胎胞爱心" primaryColour="CLOTHING_PINK_HOT" secondaryColour="CLOTHING_PINK" tertiaryColour="CLOTHING_PINK_HOT">            <tattooWriting colour="CLOTHING_PINK" glow="true"><![CDATA[精液厕所]]>                <styles>                    <style value="ITALICISED"/>                    <style value="BOLD"/>                </styles>            </tattooWriting>            <tattooCounter colour="CLOTHING_PINK" countType="NUMBERS" glow="true" type="CUM_IN_VAGINA"/>            <effects/>        </tattoo>    </tattooEntry>    <tattooEntry slot="CHEST">        <tattoo glowing="true" id="innoxia_animal_butterflies" name="蝴蝶" primaryColour="CLOTHING_PURPLE_ROYAL" secondaryColour="CLOTHING_RED_VERY_DARK" tertiaryColour="CLOTHING_PURPLE_ROYAL">            <tattooWriting colour="CLOTHING_PURPLE_ROYAL" glow="true"><![CDATA[奶牛↑]]>                <styles>                    <style value="ITALICISED"/>                    <style value="BOLD"/>                </styles>            </tattooWriting>            <tattooCounter colour="CLOTHING_PURPLE_ROYAL" countType="NUMBERS" glow="true" type="OFFSPRING_BIRTHED"/>            <effects/>        </tattoo>    </tattooEntry>    <tattooEntry slot="HIPS">        <tattoo glowing="true" id="innoxia_plant_rose" name="玫瑰" primaryColour="CLOTHING_RED_VERY_DARK" secondaryColour="CLOTHING_RED_VERY_DARK">            <tattooWriting colour="CLOTHING_RED_VERY_DARK" glow="true"><![CDATA[骚骚屁屁！]]>                <styles>                    <style value="ITALICISED"/>                    <style value="BOLD"/>                </styles>            </tattooWriting>            <tattooCounter colour="CLOTHING_RED_VERY_DARK" countType="NUMBERS" glow="true" type="CUM_IN_ASS"/>            <effects/>        </tattoo>    </tattooEntry></tattoos>""")
            node.find("character").append(new_tattoos)
            edit_count += 1
    print(f"Tattoos Setting {edit_count} Changed")

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
    edit_pet_name(npc_list)
    edit_spell(npc_list)
    edit_tattoo(npc_list)

    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print("XML saved")