from abc import abstractmethod, ABC


class Chapter(ABC):
    """Раздел меню
    Args:
        ABC (_type_): _description_
    """
    def __init__(self):
        self.name = None
        self.subsections = {} # Подразделы 

    @abstractmethod
    def functional(self):
        raise NotImplementedError
    
    def aim(self):
        """Навестись на раздел
        """
        return self.subsections

class Reference(Chapter):
    """Справка

    Args:
        Chapter (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self):
        self.subsections = "Подразделы отсутствуют"
        super().__init__()
    

    def functional(self):
        return "Справка"
    
class Edit(Chapter):
    """Правка

    Args:
        Chapter (_type_): _description_
    """
    def __init__(self):
        self.subsections = "Подразделы отсутствуют"
        super().__init__()
    

    def functional(self):
        return "Правка"



class New(Chapter):
    """Подраздел 'Новый файл'

    Args:
        Chapter (_type_): _description_
    """
    def __init__(self):
        self.name = "Новый файл"
        self.subsections = "Подразделы отсутствуют"
        super().__init__()
    

    def functional(self):
        return "Новый файл"



class Open(Chapter):
    """Подраздел 'Открыть файл'

    Args:
        Chapter (_type_): _description_
    """
    def __init__(self):
        self.name = "Открыть"
        self.subsections = "Подразделы отсутствуют"
        super().__init__()
    
    def functional(self):
        return "Открыть"


class Save(Chapter):
    """Подраздел 'Сохранить файл'

    Args:
        Chapter (_type_): _description_
    """
    def __init__(self):
        self.name = "Сохранить"
        self.subsections = "Подразделы отсутствуют"
        super().__init__()
    
    def functional(self):
        return "Сохранить"

class File(Chapter):
    """Файл

    Args:
        Chapter (_type_): _description_
    """
    def __init__(self):
        super().__init__()
    
    
    def add_chapter(self, charter:Chapter):
        self.subsections[charter.functional()] = None

    def functional(self):
        return "Файл"