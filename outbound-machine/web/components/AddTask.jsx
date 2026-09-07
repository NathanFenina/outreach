"use client";
import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { addTask } from "../app/actions";

export default function AddTask() {
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("");
  const [pending, start] = useTransition();
  const router = useRouter();

  function submit(e) {
    e.preventDefault();
    if (!title.trim()) return;
    start(async () => {
      const r = await addTask({ title, category });
      if (r.ok) {
        setTitle("");
        setCategory("");
        router.refresh();
      }
    });
  }

  return (
    <form className="addtask" onSubmit={submit}>
      <input
        className="noteInput noteInput-wide"
        placeholder="+ nouvelle tâche…"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        className="noteInput"
        placeholder="catégorie"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        style={{ width: 130 }}
      />
      <button className="addbtn" type="submit" disabled={pending || !title.trim()}>
        {pending ? "…" : "Ajouter"}
      </button>
    </form>
  );
}
