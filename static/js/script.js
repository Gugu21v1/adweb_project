function normalizeString(string) {
    return string.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

const allCategories = document.querySelectorAll(".sidebar ul li");
const categories = document.querySelectorAll(".products .product-card .product-category");

allCategories.forEach(oneCategory => {
    oneCategory.addEventListener('click', () => {
        allCategories.forEach(cat => cat.classList.remove("active"));
        oneCategory.classList.add("active");

        const selectedCategory = normalizeString(oneCategory.innerText);
        categories.forEach(productCategory => {
            const categoryText = normalizeString(productCategory.innerText);
            const isVisible = selectedCategory === "todos" || selectedCategory === categoryText;
            productCategory.closest('a').classList.toggle("d-none", !isVisible);
        });
    });
});
