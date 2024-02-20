import { API_URL } from "@lib/Enviroments";

export const getAllProducts = async (token) => {
  // let query_params = new URLSearchParams()
  // if (preferencia_id) {
  //   query_params.append('preferencia', preferencia_id)
  // }
  // const response = await fetch(`${API_URL}/productos/productos/list?${query_params}`)
  const response = await fetch(`${API_URL}/producto`, {
    headers: {
      Authorization: "Bearer " + token,
    },
  });
  const status = response.status;
  const data = await response.json();
  return { data, status };
};

export const getProductById = async (id) => {
  const response = await fetch(`${API_URL}/producto/${id}`);
  const data = await response.json();
  return data;
};

export const postProduct = async (product, image, token) => {
  let formData = new FormData();
  formData.append("nombre", product.name);
  formData.append("descripcion", product.description);
  formData.append("precio", product.price);
  formData.append("imagen", image);
  //formData.append("stock", product.stock);
  formData.append("categoria_id", product.category_id);
  formData.append("marca_id", product.category_id);
  const response = await fetch(`${API_URL}/producto`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
    body: formData,
  });
  const data = await response.json();
  return data;
};

export const uploadProductImage = async (image) => {
  let formData = new FormData();
  formData.append("imagen", image);
  const response = await fetch(`${API_URL}/producto/image/upload`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: formData,
  });
  const data = await response.json();
  return data;
};
