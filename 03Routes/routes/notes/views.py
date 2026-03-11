from rest_framework.decorators import api_view
from django.http import JsonResponse

notes_db = [
    {'id': 1, 'title': 'Note 1', 'note': 'This is note 1 content'},
    {'id': 2, 'title': 'Note 2', 'note': 'This is note 2 content'},
    {'id': 3, 'title': 'Note 3', 'note': 'This is note 3 content'},
    {'id': 4, 'title': 'Note 4', 'note': 'This is note 4 content'},
    {'id': 5, 'title': 'Note 5', 'note': 'This is note 5 content'},
    {'id': 6, 'title': 'Note 6', 'note': 'This is note 6 content'},
]


# Utility function for consistent API responses
def api_response(message, success, statuscode, data=None, **extra):
    response = {
        "message": message,
        "success": success,
        "statuscode": statuscode,
        "data": data
    }
    response.update(extra)
    return JsonResponse(response)


@api_view(['GET', 'POST'])
def notes(request):

    # ================= GET NOTES =================
    if request.method == "GET":

        search = request.GET.get("search", "").lower()
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 3))

        filtered_notes = notes_db

        # ----- Search -----
        if search:
            filtered_notes = [
                n for n in filtered_notes
                if search in n["title"].lower() or search in n["note"].lower()
            ]

        # ----- Pagination -----
        total = len(filtered_notes)
        start = (page - 1) * limit
        end = start + limit

        paginated_notes = filtered_notes[start:end]

        return api_response(
            "All notes fetched successfully",
            True,
            200,
            paginated_notes,
            page=page,
            limit=limit,
            total=total
        )

    # ================= CREATE NOTE =================
    if request.method == "POST":

        title = request.data.get("title")
        note = request.data.get("note")

        if not title or not note:
            return api_response(
                "All fields are required",
                False,
                400
            )

        new_note = {
            "id": len(notes_db) + 1,
            "title": title,
            "note": note
        }

        notes_db.append(new_note)

        return api_response(
            "Note created successfully",
            True,
            201,
            new_note
        )


# ================= GET NOTE BY ID =================
@api_view(["GET"])
def get_note_by_id(request, note_id):

    note = next((n for n in notes_db if n["id"] == note_id), None)

    if not note:
        return api_response(
            "Note not found",
            False,
            404
        )

    return api_response(
        "Note fetched successfully",
        True,
        200,
        note
    )