import requests
from abc import ABC, abstractmethod

class APIBase(ABC):
    def __init__ (self, base_url, params, timeout):
        self.__base_url = base_url
        self.__params = params
        self.__timeout = timeout

        self.__status = -1
        self.__message = None

    def get_api(self):
        try:
            resp = requests.get(self.__base_url,
                                params = self.__params,
                                timeout = self.__timeout)
            
            resp.raise_for_status() # 400 and 500 errors
            data = resp.json()

            if not data:
                raise LookupError('No to-do data')
        except requests.exceptions.RequestException as e:
            self.__message = f'A Network/HTTP error occurred {e}'
            return None
        except LookupError as e:
            self.__message = e
            return None
        except ValueError:
            self.message = 'The server response was not valid JSON'
            return None
        else:
            self.__status = 0
            return data
    
    @property
    def status(self):
        return self.__status
    
    @property
    def message(self):
        return self.__message
    
    @abstractmethod
    def call_api(self):
        ''' Ensure all inherited classes implement call_api '''
        pass

    @abstractmethod
    def __str__(self):
        pass