from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw


def create_styled_qr(data, file_name=Path("styled_qr.png"), logo_path=None, fill_color="black", back_color="white"):
    try:
        # 1. Створюємо QR-код
        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Створюємо RGB зображення
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')  # type: ignore

        if logo_path:
            logo = Image.open(logo_path).convert("RGBA")
            
            # 1. Розраховуємо розміри
            qr_width, qr_height = img.size
            # Нехай логотип займає 20% коду, а підкладка буде трохи більшою
            logo_size = int(qr_width * 0.2)
            patch_size = int(qr_width * 0.25) # Біле коло трохи більше за лого
            
            # Змінюємо розмір логотипу
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # type: ignore
            
            # 2. Малюємо круглу білу підкладку
            # Створюємо окремий шар для кола
            patch_layer = Image.new("RGBA", (patch_size, patch_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(patch_layer)
            # Малюємо заповнене біле коло
            draw.ellipse((0, 0, patch_size, patch_size), fill=back_color)
            
            # 3. Вираховуємо координати для центрування
            patch_pos = ((qr_width - patch_size) // 2, (qr_height - patch_size) // 2)
            logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            
            # 4. Накладаємо шари
            # Спочатку біле коло (використовуємо саме коло як маску)
            img.paste(patch_layer, patch_pos, mask=patch_layer)
            # Потім логотип зверху
            img.paste(logo, logo_pos, mask=logo)

        # Збереження
        img.save(file_name)
        print(f"✅ Готово! QR з круглою підкладкою збережено як: {file_name}")

    except Exception as e:
        print(f"❌ Помилка: {e}")


if __name__ == "__main__":
    link = "https://www.google.com"
    save_path = Path("output/qr_code.png")
    fill_color = "#0a9396"  # Темно-бірюзовий
    back_color = "white"
    logo_path = Path("src/assets/Google__G__logo.svg")  # Вкажіть шлях до вашого логотипу

    create_styled_qr(link, save_path, logo_path=logo_path, fill_color=fill_color, back_color=back_color)
