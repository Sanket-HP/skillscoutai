from core.firebase import db
from datetime import datetime

INVITES_COLLECTION = "invites"

def send_invite(company_id: str, candidate_id: str, role_name: str):
    invite = {
        "company_id": company_id,
        "candidate_id": candidate_id,
        "role_name": role_name,
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    db.collection(INVITES_COLLECTION).add(invite)
    return invite


def get_candidate_invites(candidate_id: str):
    invites = db.collection(INVITES_COLLECTION) \
        .where("candidate_id", "==", candidate_id) \
        .stream()

    return [invite.to_dict() for invite in invites]


def update_invite_status(invite_id: str, status: str):
    db.collection(INVITES_COLLECTION).document(invite_id).update({
        "status": status
    })
    return status
