-- 1. Отримати всі завдання певного користувача
SELECT * from tasks WHERE user_id = 3;

-- 2. Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = 2;

-- 3. Оновити статус конкретного завдання
UPDATE tasks SET status_id = 2  WHERE id = 3; 

-- 4. Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- 5. Додати нове завдання для конкретного користувача
INSERT INTO tasks(title, description, status_id, user_id) VALUES('homework', 'homework #3', 1, 4);

-- 6. Отримати всі завдання, які ще не завершено
SELECT * from tasks WHERE status_id IN (SELECT id FROM status WHERE name!='completed');

-- 7. Видалити конкретне завдання
DELETE FROM tasks WHERE id = 16;

-- 8. Знайти користувачів з певною електронною поштою
SELECT * from users WHERE email LIKE 'i.y@mail.com';
-- певна електронна пошта - це конкретна елертронна пошта
-- оскільки в нас базою гарантовано, що пошта є унікальною, то завжди буде повертатись лише одна пошта або не знайдено
-- в цьому випадку можна використовувати звичайне порівняння email='i.y@mail.com'
-- якщо потребується пошук по шаблоку, наприклад мають однаковий домен, або якась однакова послідовність у пошті
-- то треба використовувати LIKE '%seartchtext%'
SELECT * from users WHERE email LIKE '%seartchtext%';

-- 9. Оновити ім'я користувача
UPDATE users SET fullname ='name my' WHERE id = 1;

-- 10. Отримати кількість завдань для кожного статусу
SELECT COUNT(t.status_id) as task_count, s.name FROM tasks as t join status as s on s.id=t.status_id GROUP BY s.name;

-- 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT t.title, t.description, u.fullname, u.email FROM tasks as t JOIN users as u ON u.id = t.user_id  WHERE u.email LIKE '%@example.com';

-- 12. Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description = NULL;

-- 13. Вибрати користувачів та їхні завдання, які є у статусі "в процесі"
SELECT u.fullname, t.id, t.title, t.description, t.status_id  FROM tasks as t INNER JOIN users as u ON u.id = t.user_id WHERE t.status_id = 2;

-- 14. Отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.user_id) as total_tasks FROM tasks as t LEFT JOIN users as u ON t.user_id = u.id GROUP BY u.fullname;
