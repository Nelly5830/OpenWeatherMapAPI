from api_weather import APIWeather

def main():
    print('\nWelcome to the Weather App!\n')

    while True:
        city = input('Enter a city name (or type "exit" to quit): ').strip()
        if city.lower() == 'exit':
            print('\nGoodbye!')
            break

        units_choice = input('Choose units - (C)elsius or (F)ahrenheit: ').strip().lower()
        units = 'metric' if units_choice == 'c' else 'imperial'

        api = APIWeather(city, units, 10)
        status, message = api.call_api()

        if status == -1:
            print('\nAn error occurred calling the API\n')
            print(f'The error is: {message}\n')
        else:
            print(api)

if __name__ == '__main__':
    main()
