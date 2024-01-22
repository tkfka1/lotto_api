import requests
import csv

## https://dhlottery.co.kr/gameResult.do?method=byWin
## 회차 조회

def fetch_lotto_data(start_draw, end_draw):
    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    results = []

    for draw_no in range(start_draw, end_draw + 1):
        response = requests.get(f"{base_url}{draw_no}")
        if response.status_code == 200:
            data = response.json()
            if data.get("returnValue") == "success":
                results.append(data)
                print(draw_no)
            else:
                print(f"Draw {draw_no}: Data not found or error in API")
        else:
            print(f"Failed to fetch data for draw number {draw_no}")

    return results

def save_to_csv(data, filename="lotto_data.csv"):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Example usage
start_draw = 1
end_draw = 1103
lotto_data = fetch_lotto_data(start_draw, end_draw)

# Save to CSV
save_to_csv(lotto_data)