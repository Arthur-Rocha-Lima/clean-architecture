from usecases.user.find_user.find_user_dto import FindUserOutputDto
import xml.etree.ElementTree as ET

class UserPresenter:

    @staticmethod
    def toJSON(user_dto: FindUserOutputDto) -> dict:
        return {
            "id": str(user_dto.id),
            "name": user_dto.name
        }

    @staticmethod
    def toXML(user_dto: FindUserOutputDto) -> str:
        user_data = ET.Element("user")
        ET.SubElement(user_data, "id").text = str(user_dto.id)
        ET.SubElement(user_data, "name").text = str(user_dto.name)

        return ET.tostring(user_data, encoding="unicode")
    
    @staticmethod
    def toJSON_ptBR(user_dto: FindUserOutputDto) -> dict:
        return {
            "id": str(user_dto.id),
            "nome": user_dto.name
        }