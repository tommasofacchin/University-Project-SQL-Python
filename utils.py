# Utils

def sanitize_input(data):
    from main import sanitizer
    if isinstance(data, dict):
        return {key: sanitize_input(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [sanitize_input(item) for item in data]
    elif isinstance(data, str):
        return sanitizer.sanitize(data)
    return data


def allowed_file(filename):
    EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS


def db_setup(filename) -> None:
    import sqlite3
    db_path = 'instance/ecommerce.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    try:
        cursor.executescript(sql_script)
        print("DB initialized")
    except sqlite3.Error as e:
        print(f"Exception during DB initialization: {e}")
    finally:
        cursor.close()
        conn.close()
